# Use the official Node.js image as the base image
FROM node:21

# Set the working directory
WORKDIR /.

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the entire application to the working directory
COPY . .

# Start the Node.js application
CMD ["npm", "start"]
                  