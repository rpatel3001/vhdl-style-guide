
entity FIFO is

  generic (
    G_GEN1 : INTEGER;
    G_GEN2 : STD_LOGIC;
    G_GENA : t_user2;
    G_GEN3 : STD_LOGIC_VECTOR(3 downto 0);
    G_GEN4 : SIGNED(15 downto 0);
    G_GEN5 : UNSIGNED(7 downto 0);
    G_GEN6 : STD_ULOGIC;
    G_GEN7 : t_user1
  );

end entity FIFO;


-- Violation below

entity FIFO is

  generic (
    G_GEN1 : INTEGER;
    G_GEN2 : STD_LOGIC;
    G_GENA : T_USER2;
    G_GEN3 : STD_LOGIC_VECTOR(3 downto 0);
    G_GEN4 : SIGNED(15 downto 0);
    G_GEN5 : UNSIGNED(7 downto 0);
    G_GEN6 : STD_ULOGIC;
    G_GEN7 : T_USER1
  );

end entity FIFO;

-- functions passed as a generic
entity b is
  generic (
    type DATA_TYPE;
    function foo (
      a : std_logic :=0;
      b : DATA_TYPE
    ) return natural;
    impure function bar (
      a          : integer :=1;
      b          : STD_LOGIC :=32;
      constant c : std_logic
    ) return natural;
    procedure baz (
      c        : STD_LOGIC;
      signal d : in std_logic
    )
  );
end entity b;
