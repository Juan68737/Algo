Jhonathan Herrera (82264230) & Jason Guan (28702814)

Task A & Task B

to test example.in -> RUN
(first cd src)
python3 taskA.py ../input/example.in

to test example2.in -> RUN
(first cd src)
python3 taskA.py ../input/example2.in

Expected Output:

the hospital to student final match:

1 1

2 2

3 3

The time for how long the G.S took:

Timer for G.S if :0.0000057080

Error message if it was valid or not:

No erros, Valid G.S. Output

NOTE:
if you want to add more input, just make a new .in file in the input directory and make sure the first row is an N and the rest are the priority order for the hosptial and students
Example:
3
1 2 3
2 3 1
2 1 3
2 1 3
1 2 3
1 2 3

Task C: (Answer to the Task C is in the bottom and link to Google Sheets)

python3 taskC.py

we have differnet N size such as
different_n = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

and they all get run through the G.S algorithm and Validation from Task A and B. we set timers and see the amount of timer it took.

Here were the results

For Running G.S
N Time
1 0.000001625
2 0.000003208
4 0.000002959
8 0.000004791
16 0.000016625
32 0.000037125
64 0.000070708
128 0.000493583
256 0.001140875
512 0.002659917

For Validation
N Time
1 0.000002292
2 0.000002209
4 0.000002333
8 0.0000035
16 0.000006458
32 0.000012
64 0.000026792
128 0.00008325
256 0.000198708
512 0.000786833

The output was:
For N = 1
Timer for G.S is :0.0000020420
valid time was: 0.0000022920
For N = 2
Timer for G.S is :0.0000022080
valid time was: 0.0000022090
For N = 4
Timer for G.S is :0.0000036660
valid time was: 0.0000023330
For N = 8
Timer for G.S is :0.0000075000
valid time was: 0.0000035000
For N = 16
Timer for G.S is :0.0000159580
valid time was: 0.0000064580
For N = 32
Timer for G.S is :0.0000374160
valid time was: 0.0000120000
For N = 64
Timer for G.S is :0.0000769170
valid time was: 0.0000267920
For N = 128
Timer for G.S is :0.0002055830
valid time was: 0.0000832500
For N = 256
Timer for G.S is :0.0008280410
valid time was: 0.0001987080
For N = 512
Timer for G.S is :0.0035641670
valid time was: 0.0007868330

What is the trend that you notice?

The main trend that we notice is that the bigger the N, the faster it grows. When the N was 1-16, we see a steady time value where they almost all look identical but once we reach 32, then it starts increasing a bit more, until we see the major jump betweeen 64-128. This shows that the higher the N, the faster it grows

Visual graphs:

https://docs.google.com/spreadsheets/d/1qYRn4S6uP6L1rwXkUywtlg4O8-F4MzyzRGNCPCqYwMM/edit?usp=share_link
