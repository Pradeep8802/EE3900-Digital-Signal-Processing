set terminal X11 noenhanced
set title "2.8"
set xlabel "s"
set ylabel "V"
set grid
unset logscale x 
set xrange [1.000000e-13:1.000000e-05]
unset logscale y 
set yrange [-6.666644e-02:1.400000e+00]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot '../figs/2.8.data' using 1:2 with lines lw 1 title "v(2)"
