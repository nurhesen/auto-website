#!/bin/sh

if [ "$NODE_ENV" = "production" ]; then
  export REACT_APP_BASE_URL="" # Write your backend url. Mainly used for media files
  export REACT_APP_API_URL="/api" # Write your backend api url
  npm run build
else
  export REACT_APP_BASE_URL="http://localhost:8000"
  export REACT_APP_API_URL="http://localhost:8000/api"
  npm start
fi
