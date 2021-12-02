use std::path::Path;
use std::io::{self,BufRead};
use std::fs::File;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}


fn main(){
    let [mut forward,mut depth] = [0,0]; 
    if let Ok(lines) = read_lines("2.txt"){
        for line in lines{
            if let Ok(s) = line{
                let mut comm = s.split(' ');
                let c = comm.next().unwrap();
                let d:u32 = comm.next().unwrap().parse::<u32>().unwrap();
                match c {
                    "forward" => forward += d,
                    "down" => depth += d,
                    "up" => depth -= d,
                    _=> panic!(),
                };
//                println!("{:?}--{:?}",c,d);
            }
        }
    }
    println!("{}",forward*depth);
}
