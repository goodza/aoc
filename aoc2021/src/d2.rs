pub fn solve(lines:Vec<String>){
        let [mut horiz,mut depth, mut aim] = [0,0,0]; 
        println!("{:?}",lines.len());
        for line in lines{
            let mut comm = line.split(' ');
            let c = comm.next().unwrap();
            let d:u32 = comm.next().unwrap().parse::<u32>().unwrap();
            match c {
                    "forward" => {
                        horiz += d;
                        depth += aim*d;
                    },
                    "down" => aim += d,
                    "up" => aim -= d,
                    _=> panic!(),
            };
    //                println!("{:?}--{:?}",c,d);
        }
        println!("{}",horiz*depth);
}
