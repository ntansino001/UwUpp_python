
# UwUppparsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftGWEATEW_TWANEQWALL_TWOOWESS_TWANleftPWUSMINWUSleftTWIMESDIWIDErightUMINUSNOTDECWAWE DIWIDE EQWALL_TWOO EWSE GWEATEW_TWAN ID INTEGER MINWUS NOT NOTICES NUZZELS OWO PWUS STAWP STRING TWIMES WESS_TWAN WETUWN WISTEN\n    program : stmt_list\n    \n    stmt_list : stmt stmt_list\n              | empty\n    \n    stmt : DECWAWE \'*\' ID \'(\' opt_formal_args \')\' \'*\' stmt\n         | DECWAWE ID opt_init\n         | ID \'=\' exp\n         | NUZZELS exp \n         | ID \'(\' opt_actual_args \')\' \n         | WETUWN opt_exp \n         | OWO \'*\' exp \'*\' stmt STAWP\n         | \'*\' NOTICES exp \'*\' stmt opt_ewse STAWP\n         | \'{\' stmt_list \'}\'\n    \n    opt_formal_args : formal_args\n                    | empty\n    \n    formal_args : ID \',\' formal_args\n                | ID\n    \n    opt_init : \'=\' exp\n             | empty\n    \n    opt_actual_args : actual_args\n                    | empty\n    \n    actual_args : exp \',\' actual_args\n                | exp\n    \n    opt_exp : exp\n            | empty\n    \n    opt_ewse : EWSE stmt\n             | empty\n    \n    exp : exp PWUS exp\n        | exp MINWUS exp\n        | exp TWIMES exp\n        | exp DIWIDE exp\n        | exp GWEATEW_TWAN exp\n        | exp EQWALL_TWOO exp\n        | exp WESS_TWAN exp\n    \n    exp : INTEGER\n    \n    exp : WISTEN \'(\' \')\'\n    \n    exp : \'"\' STRING \'"\'\n    \n    exp : ID\n    \n    exp : ID \'(\' opt_actual_args \')\'\n    \n    exp : \'(\' exp \')\'\n    \n    exp : MINWUS exp %prec UMINUS\n    \n    exp : NOT exp\n    \n    empty :\n    '
    
_lr_action_items = {'DECWAWE':([0,3,9,11,14,18,20,24,26,27,28,32,34,36,48,53,55,57,58,59,61,62,63,64,65,66,67,68,69,70,72,79,84,86,88,89,91,],[5,5,-42,5,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,5,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,5,-38,5,-10,5,-11,-4,]),'ID':([0,3,5,8,9,11,13,14,15,16,17,18,19,20,22,24,25,26,27,28,29,32,33,34,36,41,42,43,44,45,46,47,48,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,79,81,84,86,88,89,91,],[7,7,14,24,24,7,31,-42,24,24,24,-7,24,-34,24,-37,24,-9,-23,-24,24,-5,24,-18,-6,24,24,24,24,24,24,24,-40,24,-41,-12,73,-17,7,-8,24,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,7,-38,73,7,-10,7,-11,-4,]),'NUZZELS':([0,3,9,11,14,18,20,24,26,27,28,32,34,36,48,53,55,57,58,59,61,62,63,64,65,66,67,68,69,70,72,79,84,86,88,89,91,],[8,8,-42,8,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,8,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,8,-38,8,-10,8,-11,-4,]),'WETUWN':([0,3,9,11,14,18,20,24,26,27,28,32,34,36,48,53,55,57,58,59,61,62,63,64,65,66,67,68,69,70,72,79,84,86,88,89,91,],[9,9,-42,9,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,9,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,9,-38,9,-10,9,-11,-4,]),'OWO':([0,3,9,11,14,18,20,24,26,27,28,32,34,36,48,53,55,57,58,59,61,62,63,64,65,66,67,68,69,70,72,79,84,86,88,89,91,],[10,10,-42,10,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,10,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,10,-38,10,-10,10,-11,-4,]),'*':([0,3,5,9,10,11,14,18,20,24,26,27,28,32,34,35,36,48,53,54,55,57,58,59,61,62,63,64,65,66,67,68,69,70,72,79,82,84,86,88,89,91,],[6,6,13,-42,29,6,-42,-7,-34,-37,-9,-23,-24,-5,-18,58,-6,-40,-41,72,-12,-17,6,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,6,-38,88,6,-10,6,-11,-4,]),'{':([0,3,9,11,14,18,20,24,26,27,28,32,34,36,48,53,55,57,58,59,61,62,63,64,65,66,67,68,69,70,72,79,84,86,88,89,91,],[11,11,-42,11,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,11,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,11,-38,11,-10,11,-11,-4,]),'$end':([0,1,2,3,4,9,12,14,18,20,24,26,27,28,32,34,36,48,53,55,57,59,61,62,63,64,65,66,67,68,69,70,79,86,89,91,],[-42,0,-1,-42,-3,-42,-2,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,-38,-10,-11,-4,]),'}':([3,4,9,11,12,14,18,20,24,26,27,28,30,32,34,36,48,53,55,57,59,61,62,63,64,65,66,67,68,69,70,79,86,89,91,],[-42,-3,-42,-42,-2,-42,-7,-34,-37,-9,-23,-24,55,-5,-18,-6,-40,-41,-12,-17,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,-38,-10,-11,-4,]),'NOTICES':([6,],[15,]),'=':([7,14,],[16,33,]),'(':([7,8,9,15,16,17,19,21,22,24,25,29,31,33,41,42,43,44,45,46,47,52,60,],[17,22,22,22,22,22,22,49,22,52,22,22,56,22,22,22,22,22,22,22,22,22,22,]),'INTEGER':([8,9,15,16,17,19,22,25,29,33,41,42,43,44,45,46,47,52,60,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'WISTEN':([8,9,15,16,17,19,22,25,29,33,41,42,43,44,45,46,47,52,60,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'"':([8,9,15,16,17,19,22,25,29,33,41,42,43,44,45,46,47,51,52,60,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,70,23,23,]),'MINWUS':([8,9,15,16,17,18,19,20,22,24,25,27,29,33,35,36,40,41,42,43,44,45,46,47,48,50,52,53,54,57,60,61,62,63,64,65,66,67,68,69,70,79,],[19,19,19,19,19,42,19,-34,19,-37,19,42,19,19,42,42,42,19,19,19,19,19,19,19,-40,42,19,-41,42,42,19,-27,-28,-29,-30,42,42,42,-35,-39,-36,-38,]),'NOT':([8,9,15,16,17,19,22,25,29,33,41,42,43,44,45,46,47,52,60,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'EWSE':([9,14,18,20,24,26,27,28,32,34,36,48,53,55,57,59,61,62,63,64,65,66,67,68,69,70,77,79,86,89,91,],[-42,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,84,-38,-10,-11,-4,]),'STAWP':([9,14,18,20,24,26,27,28,32,34,36,48,53,55,57,59,61,62,63,64,65,66,67,68,69,70,77,79,80,83,85,86,89,90,91,],[-42,-42,-7,-34,-37,-9,-23,-24,-5,-18,-6,-40,-41,-12,-17,-8,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,-42,-38,86,89,-26,-10,-11,-25,-4,]),')':([17,20,24,37,38,39,40,48,49,50,52,53,56,61,62,63,64,65,66,67,68,69,70,71,73,74,75,76,78,79,87,],[-42,-34,-37,59,-19,-20,-22,-40,68,69,-42,-41,-42,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,79,-16,82,-13,-14,-21,-38,-15,]),'PWUS':([18,20,24,27,35,36,40,48,50,53,54,57,61,62,63,64,65,66,67,68,69,70,79,],[41,-34,-37,41,41,41,41,-40,41,-41,41,41,-27,-28,-29,-30,41,41,41,-35,-39,-36,-38,]),'TWIMES':([18,20,24,27,35,36,40,48,50,53,54,57,61,62,63,64,65,66,67,68,69,70,79,],[43,-34,-37,43,43,43,43,-40,43,-41,43,43,43,43,-29,-30,43,43,43,-35,-39,-36,-38,]),'DIWIDE':([18,20,24,27,35,36,40,48,50,53,54,57,61,62,63,64,65,66,67,68,69,70,79,],[44,-34,-37,44,44,44,44,-40,44,-41,44,44,44,44,-29,-30,44,44,44,-35,-39,-36,-38,]),'GWEATEW_TWAN':([18,20,24,27,35,36,40,48,50,53,54,57,61,62,63,64,65,66,67,68,69,70,79,],[45,-34,-37,45,45,45,45,-40,45,-41,45,45,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,-38,]),'EQWALL_TWOO':([18,20,24,27,35,36,40,48,50,53,54,57,61,62,63,64,65,66,67,68,69,70,79,],[46,-34,-37,46,46,46,46,-40,46,-41,46,46,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,-38,]),'WESS_TWAN':([18,20,24,27,35,36,40,48,50,53,54,57,61,62,63,64,65,66,67,68,69,70,79,],[47,-34,-37,47,47,47,47,-40,47,-41,47,47,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,-38,]),',':([20,24,40,48,53,61,62,63,64,65,66,67,68,69,70,73,79,],[-34,-37,60,-40,-41,-27,-28,-29,-30,-31,-32,-33,-35,-39,-36,81,-38,]),'STRING':([23,],[51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,3,11,],[2,12,30,]),'stmt':([0,3,11,58,72,84,88,],[3,3,3,77,80,90,91,]),'empty':([0,3,9,11,14,17,52,56,77,],[4,4,28,4,34,39,39,76,85,]),'exp':([8,9,15,16,17,19,22,25,29,33,41,42,43,44,45,46,47,52,60,],[18,27,35,36,40,48,50,53,54,57,61,62,63,64,65,66,67,40,40,]),'opt_exp':([9,],[26,]),'opt_init':([14,],[32,]),'opt_actual_args':([17,52,],[37,71,]),'actual_args':([17,52,60,],[38,38,78,]),'opt_formal_args':([56,],[74,]),'formal_args':([56,81,],[75,87,]),'opt_ewse':([77,],[83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_prog','UwUpp_frontend.py',23),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','UwUpp_frontend.py',30),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','UwUpp_frontend.py',31),
  ('stmt -> DECWAWE * ID ( opt_formal_args ) * stmt','stmt',8,'p_stmt','UwUpp_frontend.py',41),
  ('stmt -> DECWAWE ID opt_init','stmt',3,'p_stmt','UwUpp_frontend.py',42),
  ('stmt -> ID = exp','stmt',3,'p_stmt','UwUpp_frontend.py',43),
  ('stmt -> NUZZELS exp','stmt',2,'p_stmt','UwUpp_frontend.py',44),
  ('stmt -> ID ( opt_actual_args )','stmt',4,'p_stmt','UwUpp_frontend.py',45),
  ('stmt -> WETUWN opt_exp','stmt',2,'p_stmt','UwUpp_frontend.py',46),
  ('stmt -> OWO * exp * stmt STAWP','stmt',6,'p_stmt','UwUpp_frontend.py',47),
  ('stmt -> * NOTICES exp * stmt opt_ewse STAWP','stmt',7,'p_stmt','UwUpp_frontend.py',48),
  ('stmt -> { stmt_list }','stmt',3,'p_stmt','UwUpp_frontend.py',49),
  ('opt_formal_args -> formal_args','opt_formal_args',1,'p_opt_formal_args','UwUpp_frontend.py',75),
  ('opt_formal_args -> empty','opt_formal_args',1,'p_opt_formal_args','UwUpp_frontend.py',76),
  ('formal_args -> ID , formal_args','formal_args',3,'p_formal_args','UwUpp_frontend.py',83),
  ('formal_args -> ID','formal_args',1,'p_formal_args','UwUpp_frontend.py',84),
  ('opt_init -> = exp','opt_init',2,'p_opt_init','UwUpp_frontend.py',94),
  ('opt_init -> empty','opt_init',1,'p_opt_init','UwUpp_frontend.py',95),
  ('opt_actual_args -> actual_args','opt_actual_args',1,'p_opt_actual_args','UwUpp_frontend.py',105),
  ('opt_actual_args -> empty','opt_actual_args',1,'p_opt_actual_args','UwUpp_frontend.py',106),
  ('actual_args -> exp , actual_args','actual_args',3,'p_actual_args','UwUpp_frontend.py',113),
  ('actual_args -> exp','actual_args',1,'p_actual_args','UwUpp_frontend.py',114),
  ('opt_exp -> exp','opt_exp',1,'p_opt_exp','UwUpp_frontend.py',124),
  ('opt_exp -> empty','opt_exp',1,'p_opt_exp','UwUpp_frontend.py',125),
  ('opt_ewse -> EWSE stmt','opt_ewse',2,'p_opt_ewse','UwUpp_frontend.py',132),
  ('opt_ewse -> empty','opt_ewse',1,'p_opt_ewse','UwUpp_frontend.py',133),
  ('exp -> exp PWUS exp','exp',3,'p_binop_exp','UwUpp_frontend.py',143),
  ('exp -> exp MINWUS exp','exp',3,'p_binop_exp','UwUpp_frontend.py',144),
  ('exp -> exp TWIMES exp','exp',3,'p_binop_exp','UwUpp_frontend.py',145),
  ('exp -> exp DIWIDE exp','exp',3,'p_binop_exp','UwUpp_frontend.py',146),
  ('exp -> exp GWEATEW_TWAN exp','exp',3,'p_binop_exp','UwUpp_frontend.py',147),
  ('exp -> exp EQWALL_TWOO exp','exp',3,'p_binop_exp','UwUpp_frontend.py',148),
  ('exp -> exp WESS_TWAN exp','exp',3,'p_binop_exp','UwUpp_frontend.py',149),
  ('exp -> INTEGER','exp',1,'p_integer_exp','UwUpp_frontend.py',156),
  ('exp -> WISTEN ( )','exp',3,'p_wisten_exp','UwUpp_frontend.py',163),
  ('exp -> " STRING "','exp',3,'p_string_exp','UwUpp_frontend.py',170),
  ('exp -> ID','exp',1,'p_id_exp','UwUpp_frontend.py',177),
  ('exp -> ID ( opt_actual_args )','exp',4,'p_call_exp','UwUpp_frontend.py',184),
  ('exp -> ( exp )','exp',3,'p_paren_exp','UwUpp_frontend.py',191),
  ('exp -> MINWUS exp','exp',2,'p_uminus_exp','UwUpp_frontend.py',198),
  ('exp -> NOT exp','exp',2,'p_not_exp','UwUpp_frontend.py',205),
  ('empty -> <empty>','empty',0,'p_empty','UwUpp_frontend.py',212),
]
