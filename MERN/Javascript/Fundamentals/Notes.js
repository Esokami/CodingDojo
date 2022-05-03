// DEBUGGING
const beatles = ["Paul", "George", "John", "Ringo"];

function printNames(names){
    function actuallyPrintingNames() {
            for (let index = 0; index < actuallyPrintingNames.length; index++){
            const name = names[index];
            console.log(name + "was found at index" + index);
        }
    }
    actuallyPrintingNames();
}
printNames(beatles);

//////////////////////////////////////////////////////////////////////

//DESTRUCTURING
// const person = {
//     firstName: "Bob",
//     lastName: "Marley",
//     email: "bob@marley.com",
//     password: "password",
//     username: "barley",
//     createdAt: 1543945177623
// };

// const animals = ["horse", "dog", "fish", "cat", "bird"];

// BEFORE ES6   
// var email = person.email;
// var firstAnimal = animals[0];

// AFTER ES6 
// const {email} = person;
// const [firstAnimal] = animals;
// console.log(email);
// // => bob@marley.com
// console.log(firstAnimal);
// => horse

// Expanding from before
// var email = person.email;
// var password = person.password;
// var firstAnimal = animals[0];
// var secondAnimal = animals[1];
// var thirdAnimal = animals[2];

// const { email, password } = person;
// const [firstAnimal, secondAnimal, thirdAnimal] = animals;

// Destructuring with the same name
// const password = '12345';
// const { password: hashedPassword } = person;

// Nested Destructuring
const person = {
    firstName: 'Bob',
    lastName: 'Marley',
    email: 'bob@marley.com',
    password: 'sekureP@ssw0rd9',
    username: 'barley',
    addresses: [
    {
        address: '1600 Pennsylvania Avenue',
        city: 'Washington, D.C.',
        zipcode: '20500',
    },
    {
        address: '221B Baker St.',
        city: 'London',
        zipcode: 'WC2N 5DU',
    }
    ],
    createdAt: 1543945177623
};

// Desctructuring Addresses
const { addresses: [whiteHouse, sherlock] } = person;

// Skip first address, get city of second; Leaving it empty allows us to skip that index
const { addresses: [ , { city: london }] } = person;
console.log(london);
// => London

////////////////////////////////////////////////////////////

// REST/SPREAD
//Using spread we can quickly make complete copies of objects or arrays
const personCopy = {...person};

//Some limitations. The copy is shallow
personCopy === person
// => false
personCopy.addresses === person.addresses
// => true

///////////////////////////////////////////////////////////

//ARROW FUNCTIONS
var sayHello = function(name) {
    console.log("Hello" + name);
};

// Re-written utilizing ES6 arrow functions, colloquially 'fat arrow' functions
const sayHello2 = (name) => {
    console.log("Hello ${name}");
};

// Single parameters don't need parenthesis and with the function body being a single statement we can remove
// the curly braces
const sayHello3 = name => console.log(`Hello ${name}`);

//More complex example
var square = function(n) {
    return n * n;
};  

// Refined
const square2 = n => n * n;

// longhand notation to return an object
// NOTE: first set of brackets are defining the function body
// and the second set of brackets are to create the object literal
const returnObjLonghand = () => {
    return { 
        firstName: 'John',
        lastName: 'Wick'
    }
}
/**
     * The example below wouldn't work because the 
     * brackets are interpreted as opening the body of the 
     * function rather than brackets to create an object literal 
     */
const returnObj = () => { firstName: 'John', lastName: 'Wick' }
// surrounding the implicit return with parenthesis solves the problem
const returnObjFixed = () => ({ firstName: 'John', lastName: 'Wick' });

//CONTEXT
// Also inherits context from parent scope
class Deck {
constructor() {
    const suits = ['Diamond', 'Heart', 'Spade', 'Club'];
    const faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'];
    const deck = [];
    for (const suit of suits) {
        for (const face of faces) {
            deck.push(this.createCard(suit, face));
        }
    }
    this.deck = deck;
}
createCard(suit, face) {
        return face + " of " + suit;
    }
}

class Deck2 {
constructor() {
    const suits = ['Diamond', 'Heart', 'Spade', 'Club'];
    const faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'];
    const deck = [];
    suits.forEach(function(suit) {
    faces.forEach(function(face) {
        deck.push(this.createCard(suit, face));
    });
    });
    this.deck = deck;
}
createCard(suit, face) {
    return face + " of " + suit;
}
}  

class Deck3 {
    constructor() {
      ... //copy variables from previous code block
      suits.forEach(suit => {
        faces.forEach(face => {
          deck.push(this.createCard(suit, face));
        });
      });
      this.deck = deck;
    }
    createCard(suit, face) {
      return face + " of " + suit;
    }
  }  

/*
 * Arrow functions don't create their own context, it looks to the enclosing scope for that information. 
 * Therefore this should now refer to the Deck instance, which has a createCard method
 */