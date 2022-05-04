/*
    The conditional (ternary) operator is the only JavaScript operator that takes three operands: 
    a condition followed by a question mark (?), then an expression to execute if the condition is truthy
    followed by a colon (:), and finally the expression to execute if the condition is falsy. 
    This operator is frequently used as a shortcut for the if statement.
 */

// BASIC IF STATEMENT
let canAfford = (itemPrice, accountBalance) => {
    if (itemPrice > accountBalance){
        return 'Cannot afford! You are $${itemPrice - accountBalance} short';
    }
    else{
        return "Can afford!";
    }
};

//TERNARY STATEMENT
let canAfford2 = (itemPrice, accountBalance) => {
    return itemPrice > accountBalance
        ? 'Cannot afford! You are $${itemPrice - accountBalance} short'
        : "Can afford";
        // is the itemPrice > accountBalance
        // yes? then return "Cannot afford"
        // no? then return "Can afford"
}

let myBankAccountBalance = 1000;
const drone = 1001;

let droneOnSale = drone - drone * 0.03;

console.log(canAfford(drone, myBankAccountBalance));
console.log(canAfford(droneOnSale, myBankAccountBalance));

console.log(canAfford2(drone, myBankAccountBalance));
console.log(canAfford2(droneOnSale, myBankAccountBalance));


/**
 * Special Note
    Take care when nesting ternary statements, as they can tend to become unwieldy and unreadable. 
    For instance, consider the following:
 */

const myVar = 10 < 20
    ? 5 < 10
        ? true
        : false
    : false

//Imagine coming back to read that code after 6 months..