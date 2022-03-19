class FreqStack {
    freq : Map<number, number> ;
    freqStack : Map<number, number[]> ;
    maxFreq : number;
    constructor() {
        this.freq = new Map();
        this.freqStack = new Map();
        this.maxFreq =0;
    }

    push(val: number): void
    {
        if( val in this.freq)
        {
            this.freq[val]++;            
        }else
        {
            this.freq[val]=1;
        }
        this.maxFreq = Math.max(this.maxFreq,this.freq[val]);

        if( this.freq[val] in this.freqStack)
        {
            this.freqStack[this.freq[val]].push(val);            
        }else
        {
            this.freqStack[this.freq[val]] = [val];
        }
    }

    pop(): number 
    {
        let val = this.freqStack[this.maxFreq].pop();
        this.freq[val]--;
        if(this.freqStack[this.maxFreq].length==0)
        {
            this.maxFreq--;
        }
        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */