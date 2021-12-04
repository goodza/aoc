pub fn solve(lines:Vec<String>){
    let mut count = 0;
    let [mut a, mut b, mut c] = [10000; 3];
    for line in lines{
        let i = line.parse().unwrap();
        if i+c+b > a+b+c { count += 1;}
        a = b;
        b = c;
        c = i;
        }
    println!("{:?}",count);
}
