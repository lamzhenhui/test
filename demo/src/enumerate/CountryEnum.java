package enumerate;
import  lombok.Getter;

public enum CountryEnum {
    ONE(1,"齐");
    @Getter private int key;
    @Getter private String value;
    CountryEnum(int key, String value){
        this.key = key;
        this.value = value;

    }



}
