#7章.类的使用

# 这里以二叉树为例子，学习类的使用
#参考 https://blog.csdn.net/Marksinoberg/article/details/69482397
import numpy as np
class BinaryTree:
	_test=1000 
	def __init__(self,rootObj=None):#儿子的，只有创建对象时候才运行，=Binary(rootobj)  self只是声明这个是对象自己的，就像c++的非static   无self=static
		self.key = rootObj#(参数给这里)  __对象变量，  对于私有属性__a,外部只能通过公有方法访问,例如__a():为私有，a()为公有
		self.leftChild = None #相当于声明一个私有属性，懂得用none,可以在普通def函数里面写self.私有变量，不一定这里
		self.rightChild = None # python里面没有私有属性这种说法，任何变量都能被调用 
		# test=1000 #类属性不能写在这里，要写在def外面
		
	#上面是儿子的数字，下面是儿子的工具箱
	def insertLeft(self,newNode):  #也是儿子的 儿子名.insertLeft调用
		if self.leftChild == None: #如果这个大儿子左边没有儿子  a=binary(b) binary叫爸爸，a叫大儿子，b是小儿子
			self.leftChild = BinaryTree(newNode) #就给大儿子的左边起一棵树，名字是参数
		else: #如果大儿子左边有小儿子
			t = BinaryTree(newNode)#则t取得新儿子
			t.leftChild = self.leftChild#大儿子的左儿子给新儿子的左边
			self.leftChild = t#当然，新儿子就成为了大儿子的左儿子
		self.takename()#调用内类函数用self, self指的是对象的takename()函数
		
	def insertRight(self,newNode): #有self指的是非静态方法，是属于对象的，无self是属于类的
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)#有点递归的感觉
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t


	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key
	def takename(self):
		print("转入类内函数")

#def __init__(self,rootObj=None) 其实r对应于self，'boy1'对应于rootObj
r=BinaryTree('boy1')
y=BinaryTree('boy3')
print('y的类属性:',y._test)  #类属性   可以类.类属性 或者 对象.类属性调用   对象优先查找 self变量，没有就到类找
print(r.getRootVal())#其实直接r.key也是可以的
r.insertLeft('boy2')
print(r.getLeftChild().getRootVal())#递归取实例方法
print(type(r))
print(len(dir(r))) #有35个属性
r.key2=12#给r实例增加了一个属性
print(len(dir(r)))#现在有36个属性了，私有
print(len(dir(r.leftChild)))#大儿子的左儿子，也只有35个属性


beau=[]
beau.append(r)
beau.append(y)
print(beau) #把节点放到一维矩阵里

#r=y #树可以赋值
#print(r.key)
r,y=y,r#互换
print(r.key)


#调用父类
#https://www.cnblogs.com/kongk/p/8644745.html

## 以下是继承的例子
class exa1():#顶层类，没有继承
	def __init__(self):#初始方法
		print('exa1_1')
	def fc():
		print('第1个的fc')
	def e2(self):
		print('第一个类的e2')
		
		
class exa2(exa1):#继承了exa1类
	aa=3
	def __init__(self):#初始方法    这里的init和fc都相当于重写，因为重名了，则按这里的为准，丢掉父类的
		print('2类初始')
	def fc():
		print('第2个的fc')#初始化时没有运行这个
	def e2(self):
		super(exa2,self).e2()#调用了父类exa1的e2
		
	
print('创建对象')
a=exa2()

print(a.fc)#a有fc，但不能运行，外部不能调用
#a.fc()#  fc如果没有self，则为类方法，内,外部不能通过对象读，都要带着类.方法或者属性调用    
#exa2.e2() 也是错的，因为e2是属于对象的，不属于类
exa2.fc()
a.e2()

print('调用2类对象的类属性',a.aa)
print(dir(a))
	
class exa3(exa1):#继承了exa1
	def __init__(self):#初始方法
		print('exa2_3')
	def fc(self):
		print('exa3_self_function')#初始化时没有运行这个
		exa1.fc()#调用继承了的类exa1中的方法(调用父类方法)
	def __len__(self):
		print('进入len')
		return 10#不能返回 str型
		
	def __getitem__(self, idx):
		print('进入getitems')
		a=[1,2,3]
		return a[idx]
	
a=exa1()
b=exa2()
#因为继承了exa1，所以实例化时，运行exa1的初始方法，但如果自己也定义了init，就运行自己的
#为重写，优先考虑本地的初始方法

c=exa3()
c.fc()


print('返回len',len(c))
print('返回getitm',c[2])

print('##########   super 用法  ##########')
class A:
	def __init__(self):
		print("5")
		print("6")
class B(A):
	def __init__(self):
		print("2")
		super(B, self).__init__()
		print("7")
class C(A):
	def __init__(self):
		print("3")
		super(C, self).__init__()#因为调用super()(B  C  D)的时候，A已经用过一次，之后都不调用,pass
		print("8")
class D(A):
	def __init__(self):
		print("4")
		super(D, self).__init__()
		print("9")
class E(B, C, D):
	def __init__(self):
		print("1")
		super(E, self).__init__()
		print("10")
E()
#调用顺序为1到10，横向 
# B  C  D 的super前
#B  C  D的super 内，但只调用一次，重复pass
#B  C  D 的super之后




# 如何调用类成员（作为全局变量）
class people():
	a=0 #静态的（共有的类成员，所以查看对象的成员属性可以看到有a,但不属于对象的，是类的）
	__b=0 #dir 对象 中找不到  
	
	
	def __init__(self):
		
		self.d=3
		people.__b+=1 #类内可以调用 类私有或者共有  类外不能调用people.__b了，对象.__b更加不行  
		people.a+=1  
test1=people()
test2=people()
test3=people()

print('dir(people):',dir(people))
print('dir(test1):',dir(test1)) #没有__b  双下划线b 封装成   _类__b  这个东西就等价成 类成员a了  完全一样   
print(people._people__b)
print(test1._people__b)
print('名字:',test1.__class__.__name__) #类名字


# print(people.__b) #类外不可调用私有
print(people.a) #创建了多少对象
print('从对象访问类成员:',test3.a)#对象对一个类，所以可以从对象访问类共有成员
#一个类对应多个对象，所以不能从类找self对象成员

#但不能 对象.类方法  外部访问  应该类.类方法访问  因为对象. 访问的时候，会自动传入self，但类方法是不接受self的
# for obj in test1.__getattribute__:
	# # if isinstance(obj, Dog): #isinstance(A,B)    指的是type(A)是否=B  或者A的类在B里面吗
	# print ('子类名字',obj.name)
print(people)
print('是他的对象吗',isinstance(test1,people))



# 1、全局变量
# 2、局部变量：在函数内、在class的方法内（未加self修饰的)
# 3、静态变量（也可以说，类属性）：在class内的，但不在class的方法内的
# 4、实例变量（也可以说，实例属性）：在class的方法内的，用self修饰的变量









