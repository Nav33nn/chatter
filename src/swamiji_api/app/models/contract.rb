class Contract < ActiveRecord::Base
#fetch
  def fetch(params)
    data = params
    #data = JSON.parse(params)
    p "---------------poi4-------------"
    if data["position"] == "max"
      query = "select name from customers order by contract_risk desc limit #{data["quantity"]}"
    else
      query = "select name from customers order by contract_risk asc limit #{data["quantity"]}"
    end
    result = ActiveRecord::Base.connection.select_rows(query).flatten!
    p "----------poi5------------------"
    local_hash = Hash.new
    local_hash["customers"] = result
    return local_hash
  end
end
