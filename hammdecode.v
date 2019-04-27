module hamming_ecoder(
	input wire clk,
    input wire a,input wire b,input wire c,input wire d,input wire e,input wire f,input wire g,
    output reg p,output reg q,output reg r,output reg s ,output reg h0,output reg h1,output reg h2 
    );
always@(posedge clk)
begin

      
    
     h0 = a ^ b ^ d ^ e;
     h1 = a ^ c ^ d ^ f;
     h2 = b ^ c ^ d ^ g;
		p=a;
		q=b;
		r=c;
		s=d;
		
    
    	r=r ^ ((!h0)*h1*h2);
    	s=s ^ (h0*h1*h2);
    	q=q ^ (h0*(!h1)*h2);
    	p=p ^ (h0*h1*(!h2));
    end
endmodule
