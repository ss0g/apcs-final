let wait = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}

let seizure = (n, ms) => {
    console.log("seizure " + n)
    if (!n) {
        return 0;
    }
    if (n % 2 == 0) {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    } else {
        document.documentElement.setAttribute("data-bs-theme", "light");
    }
    wait(ms).then(() => seizure(n - 1));
}
let seizure20100 = () => {
    seizure(20, 100);
}

document.getElementById("seizure").addEventListener("click", seizure20100);