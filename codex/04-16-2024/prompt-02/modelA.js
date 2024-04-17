for (let i = 0; i < 5; i++) {
    console.log(i); // Logs 0, 1, 2, 3, 4 
}

let count = 0;
while (count < 10) {
    console.log("Count:", count);
    count++;
}

const items = ['item1', 'item2', 'item3'];

function fetchData(item, callback) {
   // Simulate an asynchronous network request
   setTimeout(() => { 
       callback(item + " data");  
   }, 1000); 
}

for (let i = 0; i < items.length; i++) {
    fetchData(items[i], (data) => {
        console.log(data); 
    });
}