function timeInWords(h, m) {
    // Write your code here
    // Matching number to word function
    const findWord = (h) => {
        let timeString = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen","seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven","twenty eight", "twenty nine", "thirty"]
        let word = null
        for (let i = 0; i < timeString.length; i++) {
            if (h === i) {
                word = timeString[i - 1]
            }
        }
        return word
    }

    let hour = findWord(h)
    let minutes = findWord(m)
    if (m <= 30) {
        if (m === 0) {
            return `${hour} o' clock`
        } else if (m === 1) {
            return `one minute past ${hour}`
        } else if (30 > m > 0 && m !== 15) {
            return `${minutes} minutes past ${hour}`
        } else if (m === 15) {
            return `${minutes} past ${hour}`
        } else if (m === 30) {
            return `half past ${hour}`
        } 
    } else if (m > 30) {
        let convertMinutes = 60 - m 
        let hourConverted = findWord(h+1)
        let minutesConverted = findWord(convertMinutes)
        if (convertMinutes === 15) {
            return `${minutesConverted} to ${hourConverted}`
        } else {
            return `${minutesConverted} minutes to ${hourConverted}`
        }
    } 
}

console.log(timeInWords(1,1))