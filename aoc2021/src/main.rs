mod prepare;
use prepare::input::read_lines;
mod d2;
//mod d1;

fn main(){
    d2::solve(read_lines("2.txt"));
//    d1::solve(read_lines("1.txt"));
}
