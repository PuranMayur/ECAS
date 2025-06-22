# ECAS
# Efficient Cargo Allocation System
**Tags:** AVL Trees, Bin Packing, Data Structures, Algorithms, Optimization

---

## Overview

The Efficient Cargo Allocation System is a data-structure-heavy project that tackles the classical space bin packing problem with a focus on performance, modularity, and adaptability. Designed to operate under multiple constraints, the system leverages nested self-implemented AVL trees to efficiently handle:

- Bin creation and deletion  
- Cargo assignment and removal  
- Quick retrieval of bin information  

The goal is to provide logarithmic time complexity for all major operations while maintaining high flexibility for real-world cargo allocation scenarios.

---

## Features

- Nested AVL Trees: Hierarchical self-balanced binary search trees for maintaining bin metadata and cargo positions.
- Multiple Fitting Strategies: Modular implementation of strategies like First-Fit, Best-Fit, and Custom Constraint-Fit.
- Dynamic Allocation & Deletion: Efficiently handles insertion and removal of cargo in real-time.
- Optimized Utilization: Ensures maximal usage of space under varying load and capacity constraints.
- Fast Queries: Bin info and cargo placement are queryable in O(log n) time.

---
