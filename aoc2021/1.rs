use std::path::Path;
use std::io::{self,BufRead};
use std::fs::File;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}


fn main(){
    let mut count = 0;
    if let Ok(lines) = read_lines("./1.txt"){
        let mut a = 10000;
        let mut b = 10000;
        let mut c = 10000;
        for line in lines{
            if let Ok(s) = line{
                let i = s.parse().unwrap();
                if i+c+b > a+b+c {
                    count = count+1;
                }
                a = b;
                b = c;
                c = i;
            }
        }
    }
    println!("{:?}",count)
}
