# Asteroids Game

A classic Asteroids-style arcade game built with Python and Pygame, featuring modern game development patterns and clean architecture.

## 🎮 Current Status: Work in Progress

This project is actively under development. The core gameplay mechanics are implemented and functional, with ongoing work on respawn logic and game balance.

## ✨ Features Implemented

### Core Gameplay
- **Player Ship**: Triangular spaceship with rotation and movement controls
- **Asteroid Field**: Procedurally generated asteroids that spawn from screen edges
- **Shooting System**: Projectile-based combat with cooldown mechanics
- **Collision Detection**: Circle-based collision system for all game objects
- **Asteroid Splitting**: Large asteroids break into smaller pieces when destroyed
- **Lives System**: Player has 3 lives with respawn mechanics
- **Invincibility Frames**: Brief invulnerability period after respawning
- **Score Tracking**: Real-time score display and tracking

### Game Architecture
- **State Management**: Clean separation between gameplay and game over states
- **Component-Based Design**: Modular game objects with inheritance hierarchy
- **Sprite Groups**: Efficient rendering and update cycles using Pygame sprite groups
- **Event-Driven Input**: Responsive keyboard controls (WASD + Space)
- **Delta Time**: Frame-rate independent movement and timing

### User Interface
- **HUD Elements**: Score and lives display
- **Game Over Screen**: Restart and quit functionality
- **Visual Feedback**: Player ship flashing during invincibility
- **Responsive Controls**: Smooth rotation and movement

## 🚧 Currently Working On

- **Respawn Core Logic**: Fine-tuning the respawn timing and invincibility mechanics
- **Game Balance**: Adjusting asteroid spawn rates and player movement speeds
- **State Transitions**: Improving the flow between game states

## 🎯 Upcoming Features

### Gameplay Enhancements
- [ ] **Scoring System**: Point values based on asteroid size
- [ ] **Multiple Lives**: Enhanced respawn system with visual countdown
- [ ] **Explosion Effects**: Particle effects for asteroid destruction
- [ ] **Acceleration Physics**: More realistic ship movement with momentum
- [ ] **Screen Wrapping**: Objects wrap around screen edges instead of disappearing

### Visual Improvements
- [ ] **Background Image**: Space-themed background
- [ ] **Lumpy Asteroids**: Irregular asteroid shapes instead of perfect circles
- [ ] **Triangular Hitbox**: More accurate collision detection for the ship
- [ ] **Visual Polish**: Enhanced graphics and animations

### Power-ups & Weapons
- [ ] **Shield Power-up**: Temporary invincibility
- [ ] **Speed Power-up**: Enhanced movement capabilities
- [ ] **Bomb Weapon**: Area-of-effect destruction
- [ ] **Multiple Weapon Types**: Different projectile behaviors

## 🛠️ Technical Stack

- **Python 3.13+**: Modern Python features and performance
- **uv**: Fast Python package manager and project runner
- **Pygame 2.6.1**: Game development framework
- **Object-Oriented Design**: Clean, maintainable code architecture
- **Vector Mathematics**: Efficient 2D physics and collision detection

## 🎮 Controls

- **W/A/S/D**: Move and rotate the spaceship
- **Space**: Fire projectiles
- **Mouse**: Navigate menus (game over screen)

## 🚀 Getting Started

### Prerequisites
- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Pygame 2.6.1 (managed by uv)

### Installation
```bash
# Clone the repository
git clone https://github.com/Ilia01/asteroids.git
cd asteroids

# Install dependencies with uv
uv sync

# Run the game with uv
uv run game/main.py
```

## 📁 Project Structure

```
asteroids/
├── game/
│   ├── components/          # Game objects (Player, Asteroid, Shot)
│   ├── core/               # Game constants and state management
│   ├── states/             # Game state implementations
│   ├── util/               # Utility classes (UI, shapes, text)
│   └── main.py             # Entry point
├── assets/                 # Game assets (fonts, images, sounds)
├── pyproject.toml          # Project configuration
└── README.md              # This file
```

## 🎯 Development Goals

This project demonstrates:
- **Game Development Skills**: Real-time game loop, collision detection, state management
- **Software Architecture**: Clean code organization, separation of concerns
- **Python Proficiency**: Object-oriented programming, modern Python features
- **Problem Solving**: Game mechanics implementation and optimization

## 🤝 Contributing

This is a personal project showcasing game development skills. Feel free to explore the code and suggest improvements!

---

*Built with ❤️ using Python and Pygame*
