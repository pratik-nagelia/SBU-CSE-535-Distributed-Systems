package diem;

import diem.component.BlockTree;
import diem.component.Safety;

public class ClientRunner {
    public static void main(String[] args) {
        startProgram();
    }

    public static void startProgram() {
        Main main = new Main(new BlockTree(), new Safety());

//        main.processCertificateQc();
    }

}
