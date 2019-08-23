const readline = require('readline')

main()

function main() {

    var nNumbers = process.stdin.read()
    var mainArray = process.stdin.read()

    const nQueries = process.stdin.read()

    for(let i=0; i<nQueries; i++) {
        const queryArray = process.stdin.read()

        const subArray = queryArray.slice(queryArray[0], queryArray[1])

        const min = Math.min(subArray)
        console.log(min)
    }
}