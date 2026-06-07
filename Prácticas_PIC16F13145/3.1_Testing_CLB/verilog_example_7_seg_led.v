/*
// Example 1: combinatorial AND implementation:
module clb_yt_example (a, b, q);
    input a, b;
    output q;
    assign q = a & b;
endmodule

// Example 2: clocked one-bit counter that toggles only when enabled
module clb_yt_example (CLK, enable, q);
    input CLK;
    input enable;
    output reg q;
    always @(posedge CLK) begin
        if (enable) begin
            q <= !q;
        end
    end
endmodule

    Usé 4 entradas y 7 salidas.

    Este código lo extraje de youtube
*/

module clb_yt_example(
    bcd0,bcd1,bcd2,bcd3, seg0,seg1,seg2,seg3,seg4,seg5,seg6
    );

    input bcd0, bcd1, bcd2,bcd3; //initializing bcd as an 4 bit input signal
    output seg0,seg1,seg2,seg3,seg4,seg5,seg6; //initializing seg as an 8 bit output signal

    assign seg0= ~(((~bcd3)&(~bcd2)&(~bcd1)&bcd0) | ((~bcd3)&bcd2&(~bcd1)&(~bcd0))); //Logical expression for segment0 (Segment A)
    
    assign seg1= ~(((~bcd3)&bcd2&(~bcd1)&bcd0) | ((~bcd3)&bcd2&bcd1&(~bcd0))); //Logical expression for segment1 (Segment B)

    assign seg2= ~(((~bcd3)&(~bcd2)&bcd1&(~bcd0))); //Logical expression for segment2 (Segment C)
    
    assign seg3 = ~(((~bcd3)&(~bcd2)&(~bcd1)&bcd0) | ((~bcd3)&bcd2&(~bcd1)&(~bcd0)) | ((~bcd3)&bcd2&bcd1&bcd0)); //Logical expression for segment3 (Segment D)

    assign seg4 = ~(((~bcd3)&bcd0) | ((~bcd3)&bcd2&(~bcd1)) | (~(bcd2)&(~bcd1)&bcd0)); //Logical expression for segment4 (Segment E)

    assign seg5 = ~(((~bcd3)&(~bcd2)&bcd0) | ((~bcd3)&(~bcd2)&bcd1) | ((~bcd3)&bcd1&bcd0)); //Logical expression for segment5 (Segment F)

    assign seg6 = ~(((~bcd3)&(~bcd2)&(~bcd1))|((~bcd3)&bcd2&bcd1&bcd0)); //Logical expression for segment6 (Segment G)
endmodule
