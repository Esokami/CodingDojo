class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

        //Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.
        addFront(val) {

            let new_node = new Node(val);

            if(!this.head){
                this.head = new_node;
                return this;
            }

            new_node.next = this.head;

            this.head = new_node;
            return this;
        }

        // Write a method to remove the head node and return the new list head node. If the list is empty, return null.
        removeFront() {
            if (!this.head){
                return null;
            }
            var current = this.head;
            this.head = current.next;
            current.next = null;
            return this;
        }

        //Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.
        front() {
            if(this.head === null){
                return null;
            }
            else {
                return this.head.data;
            }
        }

        //Return a boolean (true/false); true, if the list possesses a node that contains the provided value.
        contains(value) {
            let runner = this.head;

            while (runner !== null){
                if (this.head.data == value){
                    return true;
                }
                else {
                    return false;
                }
            }
        }

        //Returns number of nodes in that list.
        length() {
            let runner = this.head;
            var count = 0;

            while(runner != null){
                count++;
                runner = runner.next;
            }
            return count;
        }

        //Uses a while loop and a runner to return a string containing all list values
        display() {
            let runner = this.head;
            let list = " ";

            while(runner != null){
                list += runner.data + " , " ;
                runner = runner.next;
            }
            return list;
        }

    }


let sll1 = new SLL()
sll1.addFront(18);
console.log(sll1);
// console.log(sll1.contains(18))
// console.log(sll1.contains(10))

// console.log(sll1.length());

sll1.addFront(5);
console.log(sll1);

sll1.addFront(73);
console.log(sll1);

// console.log(sll1.length());
console.log(sll1.display());

// sll1.removeFront();
// console.log(sll1);
// sll1.removeFront();
// console.log(sll1);

// sll1.front();
// console.log(sll1.front());