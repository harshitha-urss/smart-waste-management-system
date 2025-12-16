#!/usr/bin/env bash
# from project root
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
