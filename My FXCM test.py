#!/usr/bin/env python
# coding: utf-8

# In[156]:


# 1.Login
import fxcmpy
TOKEN="494d0a0ba4323d3865418701d33229a1dcb2df93"
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error')


# In[157]:


#2. Subscribe real time market price, for example “EUR/USD”, display it and save to csv file.
con.subscribe_market_data('EUR/USD')
prices=con.get_prices('EUR/USD')
prices.to_csv("prices.csv")
con.unsubscribe_market_data('EUR/USD')


# In[158]:


#3. place general market order (need to get order id and ticket id)
position = con.open_trade(symbol='EUR/USD', is_buy=True,
                       rate=1.5, is_in_pips=False,
                       amount='10', time_in_force='GTC',
                       order_type='AtMarket', limit=1.5)

order = con.create_entry_order(symbol='EUR/USD', is_buy=True,
                               amount=300, limit=1.6,
                               is_in_pips = False,
                               time_in_force='GTC', rate=1.5,
                               stop=None, trailing_step=None)


# In[159]:


print(position)


# In[160]:


OrderId = order.get_orderId()
print(OrderId)


# In[161]:


TradeId = position.get_tradeId()
print(TradeId)


# In[162]:


#4. get live open position update and display P/L change.
position=con.get_open_position(TradeId)


# In[163]:


print(position)


# In[164]:


#5. Close this open position.
position.close()


# In[165]:


#6. Retrieve closed position table and account table.
con.get_closed_positions().T


# In[166]:


con.get_accounts().T


# In[167]:


#7. logout.
con.close()

