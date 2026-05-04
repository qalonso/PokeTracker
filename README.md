# 🎮 PokéRun Platform

A comprehensive Pokémon tracking platform for collectors, shiny hunters, and challenge runners.

![Version](https://img.shields.io/badge/version-0.0.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Node](https://img.shields.io/badge/node-%3E%3D18.0.0-brightgreen.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development](#development)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

PokéRun Platform is a modern web application designed for Pokémon enthusiasts to track their:

- **Living Dex** completion across all generations
- **Shiny hunting** progress with encounter counters
- **Challenge runs** (Nuzlocke, Monotype, etc.) with team management
- **Game progression** with badges and milestones

## ✨ Features (Phase 1)

### 🔍 Complete Pokédex

- Browse all Pokémon with detailed information
- Filter by generation, type, and name
- View base stats, abilities, and evolution chains
- Support for regional forms and variants

### 📊 Collection Tracker

- Mark Pokémon as caught/uncaught
- Track completion percentage per generation
- Visual progress indicators
- Search and filter your collection

### ✨ Shiny Hunt Tracker

- Create and manage multiple shiny hunts
- Increment encounter counters
- Track hunt methods (Random Encounter, Masuda Method, Soft Reset, etc.)
- View hunt statistics and history

### 🎮 Run Manager

- Create playthroughs for different Pokémon games
- Track challenge types (Nuzlocke, Monotype, Randomizer, etc.)
- Build and manage your team
- Log badges and milestones
- Record team member nicknames and status

## 🛠️ Tech Stack

### Backend

- **NestJS** - Progressive Node.js framework
- **TypeORM** - TypeScript ORM for PostgreSQL
- **PostgreSQL** - Relational database
- **JWT** - Authentication & authorization
- **Passport** - Authentication middleware
- **class-validator** - Request validation

### Frontend

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Fast build tool
- **TanStack Query** - Server state management
- **React Router** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **Zustand** - Lightweight state management

### DevOps

- **Docker** - Containerization
- **PostgreSQL** - Database container
- **pgAdmin** - Database management UI

## 📁 Project Structure

```
pokerun-platform/
├── backend/                    # NestJS Backend API
│   ├── src/
│   │   ├── auth/              # Authentication module
│   │   ├── users/             # User management
│   │   ├── pokemon/           # Pokédex core
│   │   ├── collection/        # User collection tracking
│   │   ├── shiny-hunt/        # Shiny hunt tracker
│   │   ├── runs/              # Run management
│   │   ├── games/             # Game definitions
│   │   └── common/            # Shared utilities
│   ├── migrations/            # Database migrations
│   ├── seeds/                 # Database seeders
│   └── test/                  # Test files
│
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── api/               # API client & endpoints
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   ├── hooks/             # Custom React hooks
│   │   ├── context/           # React context providers
│   │   ├── types/             # TypeScript types
│   │   ├── utils/             # Helper functions
│   │   └── styles/            # Global styles
│   └── public/                # Static assets
│
├── docker-compose.yml         # Docker services configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** >= 18.0.0 ([Download](https://nodejs.org/))
- **npm** or **yarn**
- **PostgreSQL** >= 14 (or use Docker)
- **Git**

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/pokerun-platform.git
   cd pokerun-platform
   ```

2. **Start PostgreSQL with Docker** (recommended)

   ```bash
   docker-compose up -d postgres
   ```

   Or install PostgreSQL locally and create a database:

   ```sql
   CREATE DATABASE pokerun_db;
   ```

3. **Backend Setup**

   ```bash
   cd backend
   npm install
   cp .env.example .env
   # Edit .env file with your database credentials
   npm run migration:run
   npm run seed
   npm run start:dev
   ```

   The API will be available at `http://localhost:3000`

4. **Frontend Setup** (in a new terminal)

   ```bash
   cd frontend
   npm install
   cp .env.example .env
   # Edit .env file if needed
   npm run dev
   ```

   The app will be available at `http://localhost:5173`

### Quick Start Script

Alternatively, use the setup script:

```bash
chmod +x setup.sh
./setup.sh
```

## 💻 Development

### Backend Development

```bash
cd backend

# Start development server with hot reload
npm run start:dev

# Run tests
npm run test

# Run e2e tests
npm run test:e2e

# Generate new migration
npm run migration:generate -- -n MigrationName

# Run migrations
npm run migration:run

# Revert last migration
npm run migration:revert

# Seed database
npm run seed
```

### Frontend Development

```bash
cd frontend

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Run tests
npm run test
```

### Database Management

Access **pgAdmin** at `http://localhost:5050`:

- Email: `admin@pokerun.local`
- Password: `admin`

Add server connection:

- Host: `postgres`
- Port: `5432`
- Database: `pokerun_db`
- Username: `pokerun`
- Password: (from your .env file)

## 📚 API Documentation

Once the backend is running, visit:

- **Swagger UI**: `http://localhost:3000/api-docs`
- **Health Check**: `http://localhost:3000/health`

### Main Endpoints

```
Authentication
POST   /api/auth/register     - Register new user
POST   /api/auth/login        - Login user
POST   /api/auth/logout       - Logout user
GET    /api/auth/me           - Get current user

Pokédex
GET    /api/pokemon           - List all Pokémon (with filters)
GET    /api/pokemon/:id       - Get Pokémon details
GET    /api/pokemon/search    - Search Pokémon

Collection
GET    /api/collection        - Get user collection
POST   /api/collection/:id    - Mark Pokémon as caught
DELETE /api/collection/:id    - Mark Pokémon as uncaught

Shiny Hunts
GET    /api/shiny-hunts       - List user hunts
POST   /api/shiny-hunts       - Create new hunt
PATCH  /api/shiny-hunts/:id   - Update hunt
DELETE /api/shiny-hunts/:id   - Delete hunt

Runs
GET    /api/runs              - List user runs
POST   /api/runs              - Create new run
GET    /api/runs/:id          - Get run details
PATCH  /api/runs/:id          - Update run
DELETE /api/runs/:id          - Delete run
```

## 🗺️ Roadmap

### Phase 1 (Current) - Foundation

- [x] Project setup and architecture
- [ ] Authentication system (JWT)
- [ ] Complete Pokédex with data from PokéAPI
- [ ] User collection tracking
- [ ] Shiny hunt tracker with counter
- [ ] Basic run management system
- [ ] Team builder for runs

### Phase 2 (Future) - Enhanced Features

- [ ] Advanced statistics and analytics
- [ ] Team builder with type coverage analysis
- [ ] Import/export functionality
- [ ] Dark mode
- [ ] Mobile responsive design improvements
- [ ] Search with advanced filters

### Phase 3 (Future) - Community Features

- [ ] Public profiles
- [ ] Share collections and hunts
- [ ] Leaderboards
- [ ] Achievement system

### Phase 4 (Future) - Advanced Features

- [ ] ROM hack support
- [ ] Randomizer tracking
- [ ] AI-powered team suggestions
- [ ] Mobile app (React Native)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Environment Variables

### Backend (.env)

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=pokerun_db
DATABASE_USER=pokerun
DATABASE_PASSWORD=your_password
JWT_SECRET=your_secret_key
PORT=3000
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:3000/api
```

## 🧪 Testing

```bash
# Backend tests
cd backend
npm run test           # Unit tests
npm run test:e2e       # E2E tests
npm run test:cov       # Coverage report

# Frontend tests
cd frontend
npm run test           # Run tests
npm run test:coverage  # Coverage report
```

## 📦 Building for Production

### Backend

```bash
cd backend
npm run build
npm run start:prod
```

### Frontend

```bash
cd frontend
npm run build
# Output will be in dist/ folder
```

## 🐛 Troubleshooting

### Database connection issues

- Ensure PostgreSQL is running: `docker-compose ps`
- Check credentials in `backend/.env`
- Verify port 5432 is not in use

### Port conflicts

- Backend default: 3000 (change in `backend/.env`)
- Frontend default: 5173 (change in `frontend/vite.config.ts`)
- PostgreSQL: 5432
- pgAdmin: 5050

### Module not found errors

```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```
<!--
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PokéAPI](https://pokeapi.co/) - Pokémon data source
- [Pokémon Showdown](https://github.com/smogon/sprites) - Pokémon sprites
- NestJS and React communities 
-->

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for Pokémon trainers worldwide**
