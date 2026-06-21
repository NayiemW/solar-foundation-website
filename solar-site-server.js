#!/usr/bin/env node
/**
 * Dependency-free static server for the Solar transparency site (solar.org).
 * Replicates the clean-URL behavior the site requires (and that `npx serve`
 * provides locally), so it can run under pm2 on the node with no npm install:
 *
 *   try_files: <path>  ->  <path>.html  ->  <path>/index.html  ->  404
 *   *.html and trailing-slash URLs 301-redirect to the canonical clean URL
 *   unknown paths return a real 404 (NOT an SPA catch-all)
 *
 * Config via env: PORT (default 3100), HOST (0.0.0.0), SITE_ROOT (./solar-site).
 */
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = parseInt(process.env.PORT || "3100", 10);
const HOST = process.env.HOST || "0.0.0.0";
const ROOT = path.resolve(process.env.SITE_ROOT || path.join(__dirname, "solar-site"));

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".xml": "application/xml; charset=utf-8",
  ".txt": "text/plain; charset=utf-8",
  ".md": "text/plain; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".webp": "image/webp",
  ".ico": "image/x-icon",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
  ".ttf": "font/ttf",
  ".pdf": "application/pdf",
  ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  ".map": "application/json",
};

function resolveSafe(urlPath) {
  let p;
  try {
    p = decodeURIComponent(urlPath);
  } catch {
    return null;
  }
  const full = path.normalize(path.join(ROOT, p));
  // Stay inside ROOT (block path traversal).
  if (full !== ROOT && !full.startsWith(ROOT + path.sep)) return null;
  return full;
}

function sendText(res, status, body) {
  res.writeHead(status, { "Content-Type": "text/plain; charset=utf-8" });
  res.end(body);
}

function serveFile(req, res, file, status) {
  const ext = path.extname(file).toLowerCase();
  const type = TYPES[ext] || "application/octet-stream";
  const headers = {
    "Content-Type": type,
    "Cache-Control": ext === ".html" ? "public, max-age=0, must-revalidate" : "public, max-age=3600",
    "X-Content-Type-Options": "nosniff",
  };
  res.writeHead(status || 200, headers);
  if (req.method === "HEAD") return res.end();
  fs.createReadStream(file).pipe(res);
}

function isFile(p) {
  try {
    return fs.statSync(p).isFile();
  } catch {
    return false;
  }
}

const server = http.createServer((req, res) => {
  if (req.method !== "GET" && req.method !== "HEAD") return sendText(res, 405, "Method Not Allowed");
  let url = (req.url || "/").split("?")[0].split("#")[0] || "/";

  // Canonicalize: *.html -> clean URL.
  if (url.endsWith(".html")) {
    let clean = url.slice(0, -5);
    if (clean.endsWith("/index")) clean = clean.slice(0, -6);
    if (clean === "") clean = "/";
    res.writeHead(301, { Location: clean });
    return res.end();
  }
  // Canonicalize: trailing slash (except root) -> no slash.
  if (url.length > 1 && url.endsWith("/")) {
    res.writeHead(301, { Location: url.slice(0, -1) });
    return res.end();
  }

  const base = resolveSafe(url);
  if (base === null) return sendText(res, 400, "Bad Request");

  // try_files: exact file -> <path>.html -> <path>/index.html
  let candidates;
  if (url === "/") candidates = [path.join(ROOT, "index.html")];
  else candidates = [base, base + ".html", path.join(base, "index.html")];

  for (const c of candidates) {
    if (isFile(c)) return serveFile(req, res, c, 200);
  }

  // Honest 404 (no SPA fallback). Use 404.html if present.
  const notFound = path.join(ROOT, "404.html");
  if (isFile(notFound)) return serveFile(req, res, notFound, 404);
  return sendText(res, 404, "404 Not Found");
});

server.listen(PORT, HOST, () => {
  console.log(`solar-site static server on http://${HOST}:${PORT}  root=${ROOT}`);
});
