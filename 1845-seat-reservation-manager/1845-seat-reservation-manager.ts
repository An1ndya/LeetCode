class SeatManager {
    lastunreserved:number;
    reserved: boolean[];
    total: number;
    constructor(n: number) {
        this.total=n;
        this.lastunreserved=1;
        this.reserved = new Array(n+1).fill(false);
        //reserve
    }

    reserve(): number 
    {
        //this.lastunreserved++;
        this.reserved[this.lastunreserved]=true;
        let seat = this.lastunreserved;
        while(this.lastunreserved<=this.total && this.reserved[this.lastunreserved]==true) this.lastunreserved++;
        return seat;
    }

    unreserve(seatNumber: number): void 
    {
        this.reserved[seatNumber]=false;

        if(seatNumber<this.lastunreserved)
        {
            this.lastunreserved=seatNumber;
        }
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */