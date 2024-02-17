#!/bin/sh

if [ "$NODE_ENV" = "production" ]; then
  export REACT_APP_BASE_URL=""
  export REACT_APP_API_URL="/api"
  npm run build
else
  export REACT_APP_BASE_URL="http://localhost:8000"
  export REACT_APP_API_URL="http://localhost:8000/api"
  npm start
fi
