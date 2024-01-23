function letterCombination(n) {
    let charLetter = parseInt(n, 10);

    for (let i = 0; i <= charLetter; i++) {
        for (let j = 0; j <= charLetter; j++) {
            for (let k = 0; k <= charLetter; k++) {
                let firstLetter = String.fromCharCode(97 + i);
                let secondLetter = String.fromCharCode(97 + j);
                let thirthLetter = String.fromCharCode(97 + k);
                console.log(firstLetter, secondLetter, thirthLetter);
            }
        }
    }
}
letterCombination("3")


function countNumbers(endNumber) {
    let counter = 0;
    while (counter <= endNumber) {
        console.log(counter);
        counter++;
    }
}
countNumbers(5);


let testList = ["a", "b", "c", "d", "e"];

testList.sort((a, b) => {
    if (a > b) return -1;
    if (a < b) return 1;
    return 0;
});

for (let i = 0; i < testList.length; i++) {
    console.log("Iterratiion", i);
    console.log(testList[i]);
}


function guessTheName(name){
    name.toLowerCase() === "vasil" ? console.log("Vasil") : console.log("Somebody else");
}
guessTheName("Vasil")


