set of int: IntRange = 0..31;
set of int: GridRange = 1..6;
array[GridRange, GridRange] of var IntRange: puzzle;

% Row constraints.
constraint puzzle[1,1] + puzzle[1,2] = 7;
constraint puzzle[1,3] + puzzle[1,4] = 44;
constraint puzzle[1,5] + puzzle[1,6] = 42;

constraint puzzle[2,1] + puzzle[2,2] = 33;
constraint puzzle[2,3] + puzzle[2,4] = 8;
constraint puzzle[2,5] + puzzle[2,6] = 47;

constraint puzzle[3,1] + puzzle[3,2] = 5;
constraint puzzle[3,3] + puzzle[3,4] = 37;
constraint puzzle[3,5] + puzzle[3,6] = 15;

constraint puzzle[4,1] + puzzle[4,2] = 17;
constraint puzzle[4,3] + puzzle[4,4] = 53;
constraint puzzle[4,5] + puzzle[4,6] = 20;

constraint puzzle[5,1] + puzzle[5,2] = 9;
constraint puzzle[5,3] + puzzle[5,4] = 19;
constraint puzzle[5,5] + puzzle[5,6] = 41;

constraint puzzle[6,1] + puzzle[6,2] = 47;
constraint puzzle[6,3] + puzzle[6,4] = 26;
constraint puzzle[6,5] + puzzle[6,6] = 26;


% Column constraints.
constraint puzzle[1,1] + puzzle[2,1] = 3;
constraint puzzle[3,1] + puzzle[4,1] = 15;
constraint puzzle[5,1] + puzzle[6,1] = 25;

constraint puzzle[1,2] + puzzle[2,2] = 37;
constraint puzzle[3,2] + puzzle[4,2] = 7;
constraint puzzle[5,2] + puzzle[6,2] = 31;

constraint puzzle[1,3] + puzzle[2,3] = 29;
constraint puzzle[3,3] + puzzle[4,3] = 47;
constraint puzzle[5,3] + puzzle[6,3] = 16;

constraint puzzle[1,4] + puzzle[2,4] = 23;
constraint puzzle[3,4] + puzzle[4,4] = 43;
constraint puzzle[5,4] + puzzle[6,4] = 29;

constraint puzzle[1,5] + puzzle[2,5] = 57;
constraint puzzle[3,5] + puzzle[4,5] = 31;
constraint puzzle[5,5] + puzzle[6,5] = 25;

constraint puzzle[1,6] + puzzle[2,6] = 32;
constraint puzzle[3,6] + puzzle[4,6] = 4;
constraint puzzle[5,6] + puzzle[6,6] = 42;

% A Zero in each row at most once.
constraint forall(row in 1..6) (
  count(i in 1..6)(puzzle[row,i] = 0) <= 1
);

% A Zero in each column at most once.
constraint forall(col in 1..6) (
  count(i in 1..6)(puzzle[i,col] = 0) <= 1
);

% Flatten the 2d grid so we can run a count constraint across it.
array[1..36] of var 0..31: flat_grid = array1d(1..36, [puzzle[i,j] | i in 1..6, j in 1..6]);

% Constrain to exactly 5 zeros.
constraint count(i in 1..36)(flat_grid[i] = 0) = 5;

% Constrain to each number from 1 to 31 occurring exactly once.
constraint forall(n in 1..31) (
  count(i in 1..36)(flat_grid[i] = n) = 1
);
