class Car{
    setEngineModel(engine){
        this.engine=engine;
    }

    getEngineModel(){
        console.log(this.engine);
    }
};

class Honda extends Car{
    setCarModel(model){
        this.model=model;
    }

    getCarModel(){
        console.log(this.model);
    }
};

class Polygon{
    constructor(){
        this.sideNo=0;
        this.choice=0;
    }
    
    getChoice(){
        console.log("1. Rectangle\n2. Pentagon");
        this.choice=parseInt(prompt("Enter your choice: "));
        if(this.choice===1){
            this.sideNo=4;
            return new Rectangle();
        }
        else if(this.choice===2){
            this.sideNo=5;
            return new Pentagon();
        }
        else{
            console.log("Invalid choice");
            return null;
        }
    }
};

class Rectangle extends Polygon{
    constructor(){
        super();
        this.sideNo=4;
        this.sides=[];
    }

    inputSides(){
        for (let i=0;i<this.sideNo;i++){
            this.sides.push(parseInt(prompt(`Enter side ${i+1}: `)));
        }
        return this.sides;
    }

    displaySides(){
        for (let i=0;i<this.sideNo;i++){
            console.log(`Side ${i+1}: ${this.sides[i]}`)
        }
    }
};

class Pentagon extends Polygon{
    constructor(){
        super();
        this.sideNo=5;
        this.sides=[];
    }

    inputSides(){
        for (let i=0;i<this.sideNo;i++){
            this.sides.push(parseInt(prompt(`Enter side ${i+1}: `)));
        }
        return this.sides;
    }

    displaySides(){
        for (let i=0;i<this.sideNo;i++){
            console.log(`Side ${i+1}: ${this.sides[i]}`)
        }
    }
};

let obj=new Pentagon();
choice = obj.getChoice();
if (choice!=null){
    choice.inputSides();
    choice.displaySides();
}