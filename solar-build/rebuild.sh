#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
# build order: pages -> report -> evidence -> SEO -> unified nav
python3 build_solar.py && python3 build_report.py && python3 build_evidence.py && python3 add_seo.py && python3 unify_nav.py
echo "rebuilt solar-site"
