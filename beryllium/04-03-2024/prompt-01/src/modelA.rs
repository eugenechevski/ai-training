fn simulate_ecosystem(grid: Vec<Vec<EcosystemEntity>>, turns: usize) {
    for turn in 0..turns {
        for row in 0..grid.len() {
            for col in 0..grid[row].len() {
                let mut entity = &mut grid[row][col];
                match entity {
                    EcosystemEntity::Plant(mut energy) => {
                        energy -= 1;
                        if energy <= 0 {
                            grid[row][col] = EcosystemEntity::Empty;
                        }
                    }
                    EcosystemEntity::Herbivore(mut energy, ref mut child_count) => {
                        energy -= 1;
                        if energy <= 0 {
                            grid[row][col] = EcosystemEntity::Empty;
                        } else {
                            if child_count > 0 {
                                let new_child_pos = pick_random_position(grid);
                                if let Some(new_child) = grid[new_child_pos.0][new_child_pos.1] {
                                    grid[new_child_pos.0][new_child_pos.1] =
                                        EcosystemEntity::Herbivore(10, 0);
                                    child_count -= 1;
                                }
                            }
                            let neighbors = get_neighboring_entities(grid, row, col);
                            for neighbor in neighbors {
                                if let EcosystemEntity::Plant(mut neighbor_energy) = neighbor {
                                    energy += 1;
                                    neighbor_energy -= 1;
                                    if neighbor_energy <= 0 {
                                        grid[row][col] = EcosystemEntity::Empty;
                                    }
                                }
                            }
                        }
                    }
                    EcosystemEntity::Carnivore(mut energy, ref mut child_count) => {
                        energy -= 1;
                        if energy <= 0 {
                            grid[row][col] = EcosystemEntity::Empty;
                        } else {
                            if child_count > 0 {
                                let new_child_pos = pick_random_position(grid);
                                if let Some(new_child) = grid[new_child_pos.0][new_child_pos.1] {
                                    grid[new_child_pos.0][new_child_pos.1] =
                                        EcosystemEntity::Carnivore(10, 0);
                                    child_count -= 1;
                                }
                            }
                            let neighbors = get_neighboring_entities(grid, row, col);
                            for neighbor in neighbors {
                                if let EcosystemEntity::Herbivore(mut neighbor_energy) = neighbor {
                                    energy += 1;
                                    neighbor_energy -= 1;
                                    if neighbor_energy <= 0 {
                                        grid[row][col] = EcosystemEntity::Empty;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
