import * as fs from 'fs'

const files = fs.readdirSync("/Users/a123/Documents/GitHub/BrushTi/tool/extract_result")
console.log(files.length)

for(const fileName of files){
    const file = fs.readFileSync(`/Users/a123/Documents/GitHub/BrushTi/tool/extract_result/${fileName}`).toString()
    const matchRes = file.match("- 耳科学")
    if(matchRes){
        fs.unlinkSync(`/Users/a123/Documents/GitHub/BrushTi/tool/extract_result/${fileName}`)
        console.log(`delete file: ${fileName}`)
    } 
}


console.log(fs.readdirSync("/Users/a123/Documents/GitHub/BrushTi/tool/extract_result").length)