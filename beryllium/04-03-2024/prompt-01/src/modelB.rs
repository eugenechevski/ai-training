use std::collections::HashMap;
use std::rand::Rng;

// Define the possible entities in the ecosystem
enum EntityType {
    Plant,
    Herbivore,
    Carnivore,
}

// Define the state of each entity
struct Entity {
    energy: u32,
    type: EntityType,
}

// Define the grid of entities
struct Ecosystem {
    grid: Vec<Vec<Entity>>,
}

impl Ecosystem {
    fn new(width: u32, height: u32) -> Self {
        let mut ecosystem = Ecosystem {
            grid: Vec::new(height, Vec::new(width, Entity { energy: 100, type: EntityType::Plant })),
        };

        // Randomly add some herbivores and carnivores to the grid
        for _ in 0..(width * height * 0.1) {
            let (row, col) = (rand::rng(Rng::new()) % height, rand::rng(Rng::new()) % width);
            let mut entity = ecosystem.grid[row][col];
            entity.energy = 50;
            match rand::rng(Rng::new()) % 2 {
                0 => entity.type = EntityType::Herbivore,
                1 => entity.type = EntityType::Carnivore,
            }
        }

        ecosystem
    }

    fn update(&mut self, turn: u32) {
        for row in 0..self.grid.len() {
            for col in 0..self.grid[row].len() {
                let mut entity = &mut self.grid[row][col];

                // Deplete energy over time
                entity.energy -= 1;

                // Allow entities to eat if they are near food
                if let EntityType::Herbivore = entity.type {
                    if let Some(&mut herbivore) = self.find_nearest_entity(row, col, EntityType::Plant) {
                        herbivore.energy += 10;
                        entity.energy -= 20;
                    }
                } else if let EntityType::Carnivore = entity.type {
                    if let Some(&mut carnivore) = self.find_nearest_entity(row, col, EntityType::Herbivore) {
                        carnivore.energy += 20;
                        entity.energy -= 10;
                    }
                }

                // Allow entities to reproduce if they have enough energy
                if entity.energy >= 100 {
                    let mut new_entity = Entity { energy: 50, type: entity.type };
                    self.grid.insert(row + 1, col + 1, new_entity);
                    entity.energy -= 100;
                }

                // Allow entities to move if they have enough energy
                if entity.energy >= 20 {
                    let directions: Vec<(i32, i32)> = vec![(-1, 0), (1, 0), (0, -1), (0, 1)];
                    for (dx, dy) in directions.iter_mut() {
                        let (new_row, new_col) = (row + dx, col + dy);
                        if new_row >= 0 && new_row < self.grid.len() && new_col >= 0 && new_col < self.grid[row].len() {
                            let mut new_entity = &mut self.grid[new_row][new_col];
                            if new_entity.type == EntityType::Plant {
                                // If the new position is a plant, eat the plant and move
                                new_entity.energy -= 20;
                                entity.energy += 10;
                            } else if new_entity.type == EntityType::Herbivore || new_entity.type == EntityType::Carnivore {
                                // If the new position is another entity, fight and possibly die
                                let damage = match (entity.type, new_entity.type) {
                                    (EntityType::Herbivore, EntityType::Carnivore) |
                                    (EntityType::Carnivore, EntityType::Herbivore) => 20,
                                    _ => 0,
                                };
                                entity.energy -= damage;
                                new_entity.energy -= damage;
                                if entity.energy <= 0 || new_entity.energy <= 0 {
                                    // If either entity dies, remove it from the grid
                                    self.grid.remove(&mut self.grid[new_row][new_col]);
                                }
                            }
                        }
                    }
                    entity.energy -= 20;
                }
            }
        }
    }

    fn find_nearest_entity<T>(row: u32, col: u32, entity_type: T) -> Option<&mut Entity> {
        let mut nearest_entity: Option<&mut Entity> = None;
        let mut nearest_distance: u32 = 999999999;

        for dx in -1..=1 {
            for dy in -1..=1 {
                if dx == 0 && dy == 0 {
                    continue;
                }
                let (new_row, new_col) = (row + dx, col + dy);
                if new_row >= 0 && new_row < self.grid.len() && new_col >= 0 && new_col < self.grid[row].len() {
                    let mut entity = &mut self.grid[new_row][new_col];
                    if entity.type == entity_type {
                        let distance = (dx as f64).pow(2) + (dy as f64).pow(2);
                        if distance < nearest_distance {
                            nearest_distance = distance;
                            nearest_entity = Some(entity);
                        }
                    }
                }
            }
        }

        nearest_entity
    }
}

fn main() {
    let width = 10;
    let height = 10;
    let mut ecosystem = Ecosystem::new(width, height);

    for turn in 0..100 {
        ecosystem.update(turn);
        println!("Turn: {}", turn);
    }
}