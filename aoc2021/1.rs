use std::path::Path;
use std::io::{self,BufRead};
use std::fs::File;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}


fn main(){
    if let Ok(lines) = read_lines("./1.txt"){
        for line in lines{
            println!("{:?}",Ok(line).to_string())
        }
    }
}
