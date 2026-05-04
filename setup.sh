#!/bin/bash

echo "🎮 Setting up PokéRun Platform..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18 or higher."
    exit 1
fi

# Check Node version
NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js version 18 or higher is required. Current version: $(node -v)"
    exit 1
fi

echo -e "${GREEN}✓${NC} Node.js $(node -v) detected"

# Check if Docker is installed
if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓${NC} Docker detected"
    HAS_DOCKER=true
else
    echo -e "${YELLOW}⚠${NC} Docker not found. You'll need to install PostgreSQL manually."
    HAS_DOCKER=false
fi

echo ""
echo "📦 Installing dependencies..."
echo ""

# Backend setup
echo -e "${BLUE}[Backend]${NC} Installing dependencies..."
cd backend
if [ ! -f "package.json" ]; then
    echo "❌ Backend package.json not found. Please run 'npm init' or create the NestJS project first."
    exit 1
fi
npm install
if [ -f ".env.example" ] && [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✓${NC} Created backend/.env from template"
else
    echo -e "${YELLOW}⚠${NC} backend/.env already exists, skipping..."
fi
cd ..

# Frontend setup
echo ""
echo -e "${BLUE}[Frontend]${NC} Installing dependencies..."
cd frontend
if [ ! -f "package.json" ]; then
    echo "❌ Frontend package.json not found. Please create the React project first."
    exit 1
fi
npm install
if [ -f ".env.example" ] && [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✓${NC} Created frontend/.env from template"
else
    echo -e "${YELLOW}⚠${NC} frontend/.env already exists, skipping..."
fi
cd ..

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "📋 Next steps:"
echo ""
echo "1. ${BLUE}Configure environment variables:${NC}"
echo "   - Edit backend/.env with your database credentials"
echo "   - Edit frontend/.env if needed"
echo ""

if [ "$HAS_DOCKER" = true ]; then
    echo "2. ${BLUE}Start PostgreSQL with Docker:${NC}"
    echo "   docker-compose up -d"
    echo ""
else
    echo "2. ${BLUE}Start PostgreSQL manually${NC}"
    echo "   Install PostgreSQL and create database 'pokerun_db'"
    echo ""
fi

echo "3. ${BLUE}Run database migrations:${NC}"
echo "   cd backend && npm run migration:run"
echo ""
echo "4. ${BLUE}Seed the database:${NC}"
echo "   cd backend && npm run seed"
echo ""
echo "5. ${BLUE}Start the backend:${NC}"
echo "   cd backend && npm run start:dev"
echo ""
echo "6. ${BLUE}Start the frontend (in a new terminal):${NC}"
echo "   cd frontend && npm run dev"
echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"