module hamming_ecoder(
	input wire clk,
    input wire a,input wire b,input wire c,input wire d,
    output reg e,output reg f,output reg g, output reg h
    );
initial
begin
h<=0;

end
always@(posedge clk)
begin


     e = a^b^d;
     f = a^c^d;
     g = b^c^d;
	 
end    
endmodule
