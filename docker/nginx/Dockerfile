# step 1 as builder
# FROM node:current-alpine3.16 as build
#
# WORKDIR /app
#
# # Set working directory
# COPY ./frontend/gyanny-next-latest/client/package*.json ./
#
# # Copy all files
# COPY ./frontend/gyanny-next-latest/client/ ./
# RUN npm run build

# RUN npm ci --silent
# COPY ./frontend/gyanny-next-latest/client/ ./
# RUN npm run build
#
# # The second stage
# # Copy React static files and start nginx
FROM nginx:alpine

# RUN rm -rf /usr/share/nginx/html/*
# COPY --from=build /app/.next /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]