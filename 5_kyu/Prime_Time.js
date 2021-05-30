function prime(num) {
    // Generate an array containing every prime number between 0 and the num specified (inclusive)
    prime_list = []
        for (let number = 0; number < num; number++) {
            let div_num = 0
            for (let divisor = 0; divisor < number+1; divisor++) {
                if (number % divisor == 0) {
                    div_num += 1
                }
            }
            if (div_num == 1) {
                prime_list.push(number)
            } 
        }
    return prime_list
}

console.log('Test')