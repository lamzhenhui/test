package src.CountDownLatch;
import lombok.Getter;



public enum CountryEnum {
    One(1,"a"),Two(2,"虾"),Three(3,"球"), Four(4,"动");
    @Getter private Integer key;
    @Getter private  String value;
    CountryEnum(Integer key , String value){
        this.key = key;
        this.value = value;

    }
    public static CountryEnum forEach (int index){
        CountryEnum[]  countryEnums = CountryEnum.values();
        for (CountryEnum countryEnum : countryEnums){
            if (index == countryEnum.getKey()){
                return countryEnum;
            }
        }
        return null;
    }

}



