set of int: IntRange = 1..9;
array[IntRange, IntRange] of var IntRange: puzzle;
include "alldifferent.mzn";

% All different in rows.
constraint forall (i in IntRange) (
  alldifferent([puzzle[i,j] | j in IntRange])
);

% All different in columns.
constraint forall (i in IntRange) (
  alldifferent([puzzle[j,i] | j in IntRange])
);

% Row 1 constraints.
constraint puzzle[1,1] > puzzle[1,2];
constraint puzzle[1,3] < puzzle[1,4];
constraint puzzle[1,6] < puzzle[1,7];
constraint puzzle[1,8] = 8;
constraint puzzle[1,9] = 3;

% Row 2 constraints.
constraint puzzle[2,3] > puzzle[2,4];
constraint puzzle[2,2] = 9;
constraint puzzle[2,8] = 2;

% Row 3 constraints.
constraint puzzle[3,2] < puzzle[3,3];
constraint puzzle[3,3] < puzzle[3,4];
constraint puzzle[3,4] > puzzle[3,5];
constraint puzzle[3,5] = 6;

% Row 4 constraints.
constraint puzzle[4,2] < puzzle[4,3];
constraint puzzle[4,4] < puzzle[4,5];
constraint puzzle[4,6] > puzzle[4,7];
constraint puzzle[4,2] = 3;
constraint puzzle[4,6] = 8;

% Row 5 constraints.
constraint puzzle[5,1] > puzzle[5,2];
constraint puzzle[5,2] > puzzle[5,3];
constraint puzzle[5,7] = 7;
constraint puzzle[5,9] = 5;

% Row 6 constraints.
constraint puzzle[6,1] < puzzle[6,2];
constraint puzzle[6,4] < puzzle[6,5];
constraint puzzle[6,2] = 6;

% Row 7 constraints.
constraint puzzle[7,2] < puzzle[7,3];
constraint puzzle[7,7] < puzzle[7,8];
constraint puzzle[7,8] > puzzle[7,9];
constraint puzzle[7,4] = 1;
constraint puzzle[7,6] = 4;

% Row 8 constraints.
constraint puzzle[8,1] > puzzle[8,2];
constraint puzzle[8,6] < puzzle[8,7];
constraint puzzle[8,8] > puzzle[8,9];
constraint puzzle[8,7] = 8;
constraint puzzle[8,8] = 6;

% Row 9 constraints.
constraint puzzle[9,5] > puzzle[9,6];

% Column 1 constraints.
constraint puzzle[7,1] > puzzle[8,1];

% Column 2 constraints.
constraint puzzle[6,2] > puzzle[7,2];

% Column 4 constraints.
constraint puzzle[1,4] < puzzle[2,4];
constraint puzzle[8,4] < puzzle[9,4];

% Column 5 constraints.
constraint puzzle[3,5] < puzzle[4,5];

% Column 6 constraints.
constraint puzzle[2,6] > puzzle[3,6];
constraint puzzle[6,6] < puzzle[7,6];

% Column 7 constraints.
constraint puzzle[1,7] < puzzle[2,7];
constraint puzzle[5,7] > puzzle[6,7];
constraint puzzle[8,7] > puzzle[9,7];

% Column 8 constraints.
constraint puzzle[4,8] > puzzle[5,8];
constraint puzzle[5,8] > puzzle[6,8];

% Column 9 constraints.
constraint puzzle[1,9] < puzzle[2,9];

solve satisfy;
