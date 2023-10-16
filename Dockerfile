# Stage 1: Build the SvelteKit frontend
FROM node:14 

# Set the working directory for the frontend
WORKDIR /app

# Copy the SvelteKit frontend source code
COPY src/ ./src/
COPY package.json package-lock.json ./

# Install dependencies and build the frontend
RUN npm install
RUN npm run build

# Expose the ports for the frontend and backend
EXPOSE 5173 

# Set the working directory for the application
WORKDIR /app

# Start the Flask backend and the SvelteKit frontend
CMD ["npm", "run", "dev"]
