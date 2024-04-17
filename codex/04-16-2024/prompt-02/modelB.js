for (var i = 0; i < 5; i++) {
    setTimeout(() => {
        console.log(i);
    }, 1000);
}

for (var i = 0; i < 5; i++) {
    (function(j) {
        setTimeout(() => {
            console.log(j);
        }, 1000);
    })(i);
}

for (let i = 0; i < 5; i++) {
    setTimeout(() => {
        console.log(i);
    }, 1000);
}
