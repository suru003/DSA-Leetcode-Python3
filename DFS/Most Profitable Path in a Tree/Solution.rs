use std::collections::HashMap;

impl Solution {
    pub fn most_profitable_path(edges: Vec<Vec<i32>>, bob: i32, amount: Vec<i32>) -> i32 {
        let nodes = amount.len();

        // Build graph using HashMap
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..nodes {
            graph.insert(i as i32, Vec::new());
        }

        // Create undirected graph
        for edge in edges.iter() {
            let (a, b) = (edge[0], edge[1]);
            graph.get_mut(&a).unwrap().push(b);
            graph.get_mut(&b).unwrap().push(a);
        }

        // Initialize bob_path and path
        let mut bob_path = vec![-1; nodes];
        let mut path = vec![bob];

        // Helper function to fill Bob's path
        fn fill_bob_path(
            current: i32,
            parent: i32,
            graph: &HashMap<i32, Vec<i32>>,
            path: &mut Vec<i32>
        ) -> bool {
            if current == 0 {
                return true;
            }

            for &nbr in graph.get(&current).unwrap() {
                if nbr != parent {
                    path.push(nbr);
                    if fill_bob_path(nbr, current, graph, path) {
                        return true;
                    }
                    path.pop();
                }
            }
            false
        }

        // Fill Bob's path
        fill_bob_path(bob, -1, &graph, &mut path);

        // Mark Bob's timing at each node
        for (index, &val) in path.iter().enumerate() {
            bob_path[val as usize] = index as i32;
        }

        // Helper function for Alice's path
        fn alice_path(
            current: i32,
            parent: i32,
            current_time: i32,
            graph: &HashMap<i32, Vec<i32>>,
            bob_path: &Vec<i32>,
            amount: &Vec<i32>
        ) -> i32 {
            let mut score = 0;

            // Calculate score based on timing
            if bob_path[current as usize] > current_time || bob_path[current as usize] == -1 {
                score = amount[current as usize];
            } else if bob_path[current as usize] == current_time {
                score = amount[current as usize] / 2;
            }

            let mut local_max = i32::MIN;
            let mut went_in = false;

            // Explore all neighbors
            for &nbr in graph.get(&current).unwrap() {
                if nbr != parent {
                    went_in = true;
                    local_max = local_max.max(
                        alice_path(nbr, current, current_time + 1, graph, bob_path, amount)
                    );
                }
            }

            if went_in {
                score + local_max
            } else {
                score
            }
        }

        // Calculate and return the maximum profit
        alice_path(0, -1, 0, &graph, &bob_path, &amount)
    }
}