module hamming_ecoder(
    input [6:0] ham_in,
    output [3:0] data_out
    );
        
    wire s0,s1,s2;
    
    assign s0 = ham_in[0] ^ ham_in[1] ^ ham_in[3] ^ ham_in[4];
    assign s1 = ham_in[0] ^ ham_in[2] ^ ham_in[3] ^ ham_in[5];
    assign s2 = ham_in[1] ^ ham_in[2] ^ ham_in[3] ^ ham_in[6];
    if(s0 == 0 && s1==1 && s2==1 )
    	ham_in[2]=ham_in[2] ^ 1;
    if(s0 == 1 && s1==1 && s2==1 )
    	ham_in[3]=ham_in[3] ^ 1;
    if(s0 == 1 && s1==0 && s2==1 )
    	ham_in[1]=ham_in[1] ^ 1;
    if(s0 == 1 && s1==1 && s2==0 )
    	ham_in[0]=ham_in[0] ^ 1;

    assign data_out = {data_in[0],data_in[1],data_in[2],data_in[3]};
    
endmodule