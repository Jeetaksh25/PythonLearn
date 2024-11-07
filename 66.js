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

var obj= new Honda();
obj.setEngineModel("3.5L Twin-Turbo V6");
obj.setCarModel("Acura NSX");
obj.getEngineModel();
obj.getCarModel()