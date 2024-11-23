# Use Node.js image to build the app
FROM node:20 as build

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Expose the port Vite uses
EXPOSE 5173

# Start the Vite development server
CMD ["npm", "run", "dev","--","--host","0.0.0.0"]