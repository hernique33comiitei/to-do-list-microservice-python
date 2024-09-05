#!/bin/sh
echo "Waiting for services..."
/wait --timeout=300 --strict --host=db --port=3306 --host=redis --port=6379
echo "Services are available. Running tests..."
pytest

